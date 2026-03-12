import { useState } from 'react'
import './App.css'

function App() {

  const [inputValue, setInputValue] = useState('')
  const [results, setResults] = useState<any[]>([]) // ← état pour sto

  async function handleClick() {
    //alert(inputValue)
    const response = await fetch(`http://localhost:5000/api/search/med?molecule=${encodeURIComponent(inputValue)}`, {
      method: 'GET'
    })

    if (response.ok)
    {
      const data = await response.json()
      console.log("data from the api: ", data)
      setResults(data)
      
      for (let i = 0; i < data.length; i++)
      {
        console.log("length : ", data.length)
        console.log("length : ", data.length, JSON.stringify(data.length))

        console.log(data[i].marque)
      }

    } else if (response.status == 404){
      console.error("Erreur API:", response.status)
      //alert("Nothing found")
      setResults([]) // vide les résultats si rien trouvé
    }else if (response.status == 400){
      console.error("Erreur API:", response.status)
      //alert("Error Nothing entered")
      setResults([]) // vide les résultats si rien trouvé
    }
  }

  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault(); // bloque le rechargement
    handleClick()
  }
  
  return (
    <>
      <div>
      </div>
      <h1>Welcome to AppPharma</h1>
        <p>This app permits to search for a brand</p>
      <div id="butInput">
        <form onSubmit={handleSubmit}>
            <input
            type='text'
            placeholder='Enter the name'
            value= {inputValue}
            onChange={(e)=> setInputValue(e.target.value)}>
            </input>
            <button type="submit">Search</button>
        </form>
      </div>

      <div id="result">
        {results.length > 0 ? (
          <ul>
            {results.map((item, index) =>
            (
              <li id="megaliste" key={index}> {item.molecule} -- <strong> {item.marque}</strong></li>
            ))}
          </ul>
        ):
        (<p> No results yet </p>)
        }
      </div>
    </>
  )
}

export default App
