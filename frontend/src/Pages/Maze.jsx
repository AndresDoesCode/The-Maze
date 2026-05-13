import "../css/Maze.css"

export default function Maze({grid, rows, columns}){
    const divStyle1 = {
        backgroundColor: "#4F46E5",
    };

    const divStyle2 = {
        backgroundColor: "#DAA520",
    };


    return(
    <>  
            <div 
                className="Grid-Container"
                style={{
                    gridTemplateRows: `repeat(${rows}, 1fr)`
                }}
            >
                {grid.map((row, rowIndex)=>(
                    <div
                        className="Grid-Row"
                        key={rowIndex}
                        style={{
                            gridTemplateColumns: `repeat(${columns}, 1fr)`
                        }}
                    >
                        {row.map((bitValue, colIndex)=>(
                            /* Here is where the actual cell is */
                            <div 
                                key={`${rowIndex}-${colIndex}`}
                                className={`
                                    Grid-Cell
                                    ${bitValue & 1 ? "border-top" : ""}
                                    ${bitValue & 2 ? "border-right" : ""}
                                    ${bitValue & 4 ? "border-bottom" : ""}
                                    ${bitValue & 8 ? "border-left" : ""}
                                `}
                            >
                                {bitValue & 16 ? <div className="Ball"/> : null}
                                {bitValue & 32 ? <div className="Bit"/> : null}
                            </div>
                        ))}
                    </div>
                ))}   
            </div>    
        </>
    )
}