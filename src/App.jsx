import { useState } from 'react'
import './App.css'
import { images } from './services/GetImages'


function App() {
  const [count, setCount] = useState(0)
  // console.log(images);
  // images = record.then(data => data.json())
  console.log(import.meta.env.VITE_API_URL)
  return (
    <div className="App">
      
     
    </div>
  )
}

export default App
