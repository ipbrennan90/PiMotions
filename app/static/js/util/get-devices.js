export const getMedia = (navigator, cb) => {
    window.navigator.mediaDevices.getUserMedia({video: true})
        .then(cb)
        .catch(e => console.error(e))
}

