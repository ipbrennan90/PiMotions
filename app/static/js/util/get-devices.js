export const getMedia = (navigator, cb) => {
    const mediaGetter = navigator.mediaDevices.getUserMedia ||
          navigator.mediaDevices.webkitGetUserMedia ||
          navigator.mediaDevices.mozGetUserMedia
    mediaGetter({video: true})
        .then(cb)
        .catch(e => console.error(e))
}
