import { useState } from 'react'
import './App.css'

function App() {

  const [inputValue, setInputValue] = useState('')
  //onst [results, setResults] = useState([])  // ← ÉTAT MANQUANT

  async function handleClick() {
    //alert(inputValue)
    const response = await fetch(`http://localhost:5000/api/search/med?molecule=${encodeURIComponent(inputValue)}`, {
      method: 'GET'
    })

    if (response.ok)
    {
      const data = await response.json()
      console.log("data from the api: ", data)
      
      for (let i = 0; i < data.length; i++)
      {
        console.log("length : ", data.length)
        console.log("length : ", data.length, JSON.stringify(data.length))

        console.log(data[i].marque)
      }

    } else if (response.status == 404){
      console.error("Erreur API:", response.status)
      alert("Nothing found")
    }else if (response.status == 400){
      console.error("Erreur API:", response.status)
      alert("Error Nothing entered")
    }
  }
  return (
    <>
      <div>
      </div>
      <h1>Welcome to AppPharma</h1>
        <p>This app permits to search for a brand</p>
      <div id="butInput">
        <input
        type='text'
        placeholder='Enter the name'
        value= {inputValue}
        onChange={(e)=> setInputValue(e.target.value)}>
        </input>
        <button onClick={handleClick}>Search</button>
      </div>
    </>
  )
}

export default App
