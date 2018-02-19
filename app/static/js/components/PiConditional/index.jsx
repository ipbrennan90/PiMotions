import React from 'react'
import PropTypes from 'prop-types'
import './style.css'

const PiConditional = ({chooseCam}) => (
  <div className="pi_conditional">
    <p>Use camera on pi?</p>
    <button
      onClick={() => {
        chooseCam('pi')
      }}
    >
      YES
    </button>
    <button
      onClick={() => {
        chooseCam('web')
      }}
    >
      NO
    </button>
  </div>
)

PiConditional.propTypes = {
  chooseCam: PropTypes.func,
}

export default PiConditional
