import { StrictMode } from 'react'
import "../css/Game_Selection.css"

function Game_Selection(){
    return(
        <>
            <div className='GS_Container'>
                <div className='GS_Title'>
                    <h1 style={{fontSize: '3em'}}>The Maze</h1>
                </div>
                <div className='GS_Button_Alignment'>
                    <button className='GS_Button'>
                        <p style={{fontSize: '1.5em'}}>Play Game</p>
                    </button>
                    <button className='GS_Button'>
                        <p style={{fontSize: '1.5em'}}>Reset Progress</p>
                    </button>
                    <button className='GS_Button'>
                        <p style={{fontSize: '1.5em'}}>How to Play</p>
                    </button> 
                </div>
            </div>
        </>
    )
}

export default Game_Selection