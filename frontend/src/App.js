import React, { useState } from 'react'
import { Button } from 'react-bootstrap'
import AcceptMaxFiles from './components/Dropzone'
import styled from 'styled-components'
import API from './axios'

const Wrapper = styled.div`
	margin: 0;
	padding: 50px;
`

const DropzoneContainer = styled.div`
	margin: 0 auto;
	text-align: center;
	height: 100%;
	display: flex;
	flex-direction: column;
	row-gap: 30px;
`

const CenterLine = styled.hr`
	width: 80%;
	margin: 70px auto;
`

const ResultContainer = styled.div`
	text-align: center;
	margin: 0 auto;
	height: 100%;
	display: flex;
	flex-direction: column;
	row-gap: 20px;
	border-radius: 8px;
	border: 1px solid black;
	width: 90%;
	padding: 20px;
`

const ResultChildContainer = styled.div`
	display: flex;
	flex-direction: row;
	column-gap: 40px;
	justify-content: center;
`

const ResultTextContainer = styled.div`
	text-align: start;
	font-size: 18px;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
`

const App = () => {
	const [files, setFiles] = useState([])
	const [predictedResults, setPredictedResults] = useState([])

	const onPredict = async () => {
		const form = new FormData()
		files.forEach((file) => form.append('predicted-pictures', file))

		const { data, status } = await API({
			url: '/predict',
			data: form,
		})
		if (status === 400 || status === 500) {
			alert('Oops! Something Went Wrong. Please try again. :(')
		} else if (status === 200) {
			setPredictedResults((prevState) => [...prevState, ...data])
		}
	}

	return (
		<Wrapper>
			<DropzoneContainer>
				<h1 style={{ textDecoration: 'underline', fontWeight: 'bold' }}>
					5 files are the maximum number of files you can drop here
				</h1>
				<AcceptMaxFiles files={files} setFiles={setFiles} />
				<Button
					onClick={() => files.length > 0 && onPredict()}
					style={{
						width: '40%',
						margin: '0 auto',

						cursor: files.length > 0 ? 'pointer' : 'not-allowed',
					}}
					size='lg'
				>
					Predict a Papaya
				</Button>
			</DropzoneContainer>

			<CenterLine />

			<ResultContainer>
				<h2 style={{ textDecoration: 'underline', fontWeight: 'bold' }}>Prediction Summary</h2>
				{files.map((file) => (
					<ResultChildContainer>
						<img src={file?.preview} alt={file?.name} width='240' />
						<ResultTextContainer>
							<p>Ripeness: </p>
							<p>Percentage: 50%</p>
						</ResultTextContainer>
					</ResultChildContainer>
				))}
			</ResultContainer>
		</Wrapper>
	)
}

export default App
