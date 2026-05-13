import "../css/test_level.css"
import Maze from "./Maze.jsx"
import {useState, useEffect} from "react"

export default function test_level(){
    const [data, setData] = useState();

    useEffect(()=>{
        const get_level_data = async () =>{
            //Full route :(
            try {
                const level_url = "http://127.0.0.1:5001/Test"

                const res = await fetch(level_url)
                const data = await res.json()
                setData(data)
                
                console.log(data)
            } catch (err) {
                console.log(`This is how we messed up :( ${err}`)
            }
        }

        get_level_data();

        // return () => {
        //     console.log("Optional clean up function")
        // }
    }, []);

    return (
        <>
            {data ? 
                <>
                    <p>{data?.Level}</p>
                    <Maze grid={data?.Maze} rows={data?.num_row} columns={data?.num_col} />
                </>
            
            
            : <p>Loading...</p>}
        </>
    )
}

