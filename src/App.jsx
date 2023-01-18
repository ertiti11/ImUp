import { useState } from 'react'
import './App.css'
import ImageList from './components/ImageList.jsx/ImageList'
import { images } from './services/GetImages'


function App() {
  const [count, setCount] = useState(0)
  // console.log(import.meta.env.VITE_API_URL)
  return (
    <div className="App">
      <ImageList />
     
    </div>
  )
}

export default App
