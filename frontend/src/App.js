import React, { useState } from 'react'
import AcceptMaxFiles from './components/Dropzone'
import { Card, CardBody, CardButton } from './components/Card'

import API from './axios'

function App() {
  const [files, setFiles] = useState([])

  const onPredict = async () => {
    const res = await API.post('')
  }

  return (
    <Card>
      <CardBody>
        5 files are the maximum number of files you can drop here
        <AcceptMaxFiles files={files} setFiles={setFiles} />
        <CardButton onClick={() => {}}>Predict</CardButton>
      </CardBody>
    </Card>
  )
}

export default App
