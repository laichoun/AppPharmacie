import './App.css'

async function handleClick() {
  alert("Hello")
 //await fetch = 
}

function App() {
  return (
    <>
      <div>
      </div>
      <h1>Welcome to AppPharma</h1>
        <p>This app permits to search for a brand</p>
      <div id="butInput">
        <input type='text'
        placeholder='Enter the name'>
        </input>
        <button onClick={handleClick}>Search</button>
      </div>
    </>
  )
}

export default App
