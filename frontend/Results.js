export default function Results({results}){

    return(

        <div>

            {results.map(x=>(

                <div key={x.id}
                style={{
                    border:"1px solid #ddd",
                    margin:"10px",
                    padding:"10px"
                }}>

                    <h3>
                        {x.brand} {x.model}
                    </h3>

                    <p>{x.cpu}</p>

                    <p>{x.ram} GB</p>

                    <p>{x.storage}</p>

                    <p>{x.price} SAR</p>

                    <a href={x.url}>
                        Open Store
                    </a>

                </div>

            ))}

        </div>

    );

}