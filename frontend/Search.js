import {useState} from "react";
import Results from "./Results";

export default function Search(){

    const API = process.env.REACT_APP_API;

    const [filters,setFilters] = useState({});
    const [results,setResults] = useState([]);

    const update = (key,value)=>{
        setFilters({...filters,[key]:value});
    }

    const search = async ()=>{

        const res = await fetch(API+"/search",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(filters)
        });

        const data = await res.json();

        setResults(data);
    }

    return(

        <div>

            <select onChange={(e)=>update("ram",parseInt(e.target.value))}>
                <option value="">RAM</option>
                <option value="8">8</option>
                <option value="16">16</option>
                <option value="32">32</option>
            </select>

            <select onChange={(e)=>update("storage_size",parseInt(e.target.value))}>
                <option value="">Storage</option>
                <option value="256">256</option>
                <option value="512">512</option>
                <option value="1024">1TB</option>
            </select>

            <select onChange={(e)=>update("cpu_brand",e.target.value)}>
                <option value="">CPU</option>
                <option value="Intel">Intel</option>
                <option value="AMD">AMD</option>
            </select>

            <button onClick={search}>
                Search
            </button>

            <Results results={results}/>

        </div>

    );

}