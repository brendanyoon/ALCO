const canvas = document.querySelector('canvas')
const c = canvas.getContext('2d')

canvas.width = 800
canvas.height = 400


const gravity = 0.7

class Sprite {
    constructor ({ position, velocity, color = 'red', offset}) {
        this.position = position
        this.velocity = velocity
        this.width = 40
        this.height = 100
        this.lastKey
        this.attackBox = {
            position: {
                x: this.position.x,
                y: this.position.y
            },
            offset,
            width: 80,
            height: 40
        }
        this.color = color
        this.isAttacking = false
        this.health = 100
    }

    draw () {
        c.fillStyle = this.color
        c.fillRect(this.position.x, this.position.y, this.width, this.height)

        //attack box is drawn here
        if (this.isAttacking) {
            c.fillStyle = 'green'
            c.fillRect(this.attackBox.position.x, this.attackBox.position.y, this.attackBox.width, this.attackBox.height)
        }
    }

    update() {
        this.draw()
        this.attackBox.position.x = this.position.x + this.attackBox.offset.x
        this.attackBox.position.y = this.position.y

        this.position.x += this.velocity.x
        this.position.y += this.velocity.y

        if (this.position.y + this.height + this.velocity.y >= canvas.height) {
            this.velocity.y = 0
        } else {
            this.velocity.y += gravity
        }
    }

    attack () {
        this.isAttacking = true
        setTimeout(() => {
            this.isAttacking = false
        }, 100)
    }
}

const player = new Sprite ({
    position: {
        x: 0,
        y: 0
    },
    velocity: {
        x: 0,
        y: 0
    },
    offset: {
        x: 0,
        y: 0
    }
})

const enemy = new Sprite ({
    position: {
        x: 400,
        y: 100
    },
    velocity: {
        x: 0,
        y: 0
    },
    color: 'blue',
    offset: {
        x: -40,
        y: 0
    }
})


console.log(player)

const keys = {
    a: {
        pressed:false
    },
    d: {
        pressed:false
    },

    j: {
        pressed:false
    },
    l: {
        pressed:false
    }
}

function rectCollision({ rect1, rect2 }) {
    return (
        rect1.attackBox.position.x + rect1.attackBox.width >= rect2.position.x &&
        rect1.attackBox.position.x <= rect2.position.x + rect2.width &&
        rect1.attackBox.position.y + rect1.attackBox.height >= rect2.position.y &&
        rect1.attackBox.position.y <= rect2.position.y + rect2.height
        )
}

function determineWinner({ player, enemy, timerID}) {
    clearTimeout(timerID)
    document.querySelector('#displayText').style.display = 'flex'
    if (player.health === enemy.health) {
        document.querySelector('#displayText').innerHTML = 'Tie'
    } else if (player.health > enemy.health) {
        document.querySelector('#displayText').innerHTML = 'Player 1 Wins!'
    } else
        document.querySelector('#displayText').innerHTML = 'Player 2 Wins!'
}

let timer = 60
let timerID
function decreaseTimer () {
    if (timer > 0) {
        timerID = setTimeout(decreaseTimer, 1000)
        timer--
        document.querySelector('#timer').innerHTML = timer
    }

    if (timer === 0) {
        determineWinner({ player, enemy, timerID })
    }
}

decreaseTimer()

function animate() {
    window.requestAnimationFrame(animate)
    c.clearRect(0, 0, canvas.width, canvas.height)
    player.update()
    enemy.update()

    player.velocity.x = 0
    enemy.velocity.x = 0

    //player movement
    if (keys.d.pressed && player.lastKey === 'd') {
        player.velocity.x = 5
    } else if (keys.a.pressed && player.lastKey === 'a') {
        player.velocity.x = -5
    }

    //enemy movement
    if  (keys.j.pressed && enemy.lastKey === 'j') {
        enemy.velocity.x = -5
    } else if (keys.l.pressed && enemy.lastKey === 'l') {
        enemy.velocity.x = 5
    }

    //detect for collision (hit)
    if (rectCollision({ rect1: player, rect2: enemy }) && player.isAttacking) {
        player.isAttacking = false
        enemy.health -= 20
        document.querySelector('#enemyHealth').style.width = enemy.health + '%'
    }

    if (rectCollision({ rect1: enemy, rect2: player }) && enemy.isAttacking) {
        enemy.isAttacking = false
        player.health -= 20
        document.querySelector('#playerHealth').style.width = player.health + '%'
    }

    if (enemy.health <= 0 || player.health <= 0) {
        determineWinner({ player, enemy, timerID })
    }

}

animate()

window.addEventListener('keydown', (event) => {
    switch (event.key) {
        case 'd':
            keys.d.pressed = true
            player.lastKey = 'd'
            break
        case 'a':
            keys.a.pressed = true
            player.lastKey = 'a'
            break
        case 'w':
            player.velocity.y = -15
            break
        case 's':
            player.attack()
            break

        case 'l':
            keys.l.pressed = true
            enemy.lastKey = 'l'
            break
        case 'j':
            keys.j.pressed = true
            enemy.lastKey = 'j'
            break
        case 'i':
            enemy.velocity.y = -15
            break
        case 'k':
            enemy.attack()
            break
    }

})

window.addEventListener('keyup', (event) => {
    switch (event.key) {
        case 'd':
            keys.d.pressed = false
            break
        case 'a':
            keys.a.pressed = false
            break

        case 'l':
            keys.l.pressed = false
            break
        case 'j':
            keys.j.pressed = false
            break
    }

})