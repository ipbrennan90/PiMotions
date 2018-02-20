export const snapshot = (camera, context) => {
  camera
    .snapshot()
    .then(data => {
      context.setState({ image: data })
    })
    .catch(console.error)
}
