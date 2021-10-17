import React from 'react'
import AcceptMaxFiles from './components/Dropzone'

function App() {
  return (
    <div>
      5 files are the maximum number of files you can drop here
      <AcceptMaxFiles />
      <button onClick={() => {}}>Predict</button>
    </div>
  )
}

export default App
