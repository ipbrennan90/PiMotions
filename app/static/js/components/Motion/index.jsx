import React from 'react'
import PropTypes from 'prop-types'
import './style.css'

const Motion = ({
  turnOnMotion,
  motionDetector,
  motionWidth,
  motionBackground,
  sensitivity,
  handleSensitivityChange,
  threshold,
  handleThresholdChange,
}) => (
  <div className="wrapper">
    <button className="button trigger" onClick={turnOnMotion}>
      TURN MOTION DETECTOR {motionDetector === 'on' ? 'OFF' : 'ON'}
    </button>
    <div className="motionbar">
      <div
        className="motiondetected"
        style={{
          width: `${motionWidth}%`,
          backgroundColor: `${motionBackground}`,
        }}
      />
    </div>
    <label className="sliderlabel" htmlFor="sensitivity">
      sensitivity: {sensitivity}
    </label>
    <input
      type="range"
      onMouseUp={handleSensitivityChange}
      id="sensitivity"
      min="0"
      defaultValue="20"
      max="500"
      step="1"
      className="slider"
    />
    <label className="sliderlabel" htmlFor="threshold">
      threshold: {threshold}
    </label>
    <input
      type="range"
      onMouseUp={handleThresholdChange}
      id="threshold"
      min="0"
      defaultValue="10"
      max="500"
      step="1"
      className="slider"
    />
  </div>
)

Motion.propTypes = {
  turnOnMotion: PropTypes.func,
  motionDetector: PropTypes.string,
  motionWidth: PropTypes.number,
  motionBackground: PropTypes.string,
  sensitivity: PropTypes.oneOfTyoe([string, number]),
  handleSensitivityChange: PropTypes.func,
  threshold: PropTypes.oneOfTyoe([string, number]),
  handleThresholdChange: PropTypes.func,
}

export default Motion
