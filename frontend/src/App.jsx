import { Route,Routes } from 'react-router-dom'
import Game_Selection from './Pages/Game_Selection'
import "./css/Global.css"
import T1 from './Pages/test_level'

function App() {
  return (
    <>
      <Routes>
        <Route index element={<T1/>}/>
      </Routes>
    </>
  )
}

export default App
