import { Route,Routes } from 'react-router-dom'
import Game_Selection from './Pages/Game_Selection'
import './css/App.css'

function App() {
  return (
    <>
      <Routes>
        <Route index element={<Game_Selection/>}/>
      </Routes>
    </>
  )
}

export default App
