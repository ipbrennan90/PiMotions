import React from 'react'
import PropTypes from 'prop-types'
import ReactCamera from 'simple-react-camera'

const Camera = ({innerRef}) => (
  <div className="image_container">
    {!takeOnPi && (
      <ReactCamera
        className={'yourCssClassHere'}
        ref={innerRef}
        width={800}
        height={500}
      />
    )}
    <img className="image" src={this.state.image} />
  </div>
)

Camera.propTypes = {
  innerRef: PropTypes.func,
}

export default Camera
