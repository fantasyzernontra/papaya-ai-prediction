import React, { useState } from 'react'
import AcceptMaxFiles from './components/Dropzone'

import API from './axios'

function App() {
	const [files, setFiles] = useState([])

	const onPredict = async () => {
    const res = await API.post('')
  }

	return (
		<div>
			5 files are the maximum number of files you can drop here
			<AcceptMaxFiles files={files} setFiles={setFiles} />
			<button onClick={() => {}}>Predict</button>
		</div>
	)
}

export default App
