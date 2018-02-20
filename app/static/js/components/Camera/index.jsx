import React from 'react'
import PropTypes from 'prop-types'
import ReactCamera from 'simple-react-camera'

const Camera = ({ innerRef, takeOnPi, image }) => (
  <div className="image-container">
    {takeOnPi ? (
      <img className="image" src={image} />
    ) : (
      <ReactCamera
        className={'yourCssClassHere'}
        ref={innerRef}
        width={800}
        height={500}
      />
    )}
  </div>
)

Camera.propTypes = {
  innerRef: PropTypes.func,
  takeOnPi: PropTypes.bool,
  image: PropTypes.string
}

export default Camera
