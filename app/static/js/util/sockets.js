import io from 'socket.io-client'
const socket = io(process.env.RASPI_URL)

const addSocketEvent = (message,callback) => {
    socket.on(message,  (data) => {callback(data)})
}

export const listen = (events) => {
    events.forEach((event) => {
        addSocketEvent(event.message, event.callback)
    })
}
        
        
