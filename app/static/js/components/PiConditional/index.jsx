import React from 'react'
import PropTypes from 'prop-types'
import './style.css'

const PiConditional = ({ chooseCam }) => (
  <div>
    <h3 className="center">Image Source</h3>
    <div className="pi-conditional">
      <input
        type="radio"
        name="camera"
        id="option-1"
        value="pi"
        defaultChecked
        onChange={chooseCam}
      />
      <label htmlFor="option-1">R Pi</label>

      <input
        type="radio"
        name="camera"
        id="option-2"
        value="web"
        onChange={chooseCam}
      />
      <label htmlFor="option-2">Webcam</label>
    </div>
  </div>
)

PiConditional.propTypes = {
  chooseCam: PropTypes.func
}

export default PiConditional
