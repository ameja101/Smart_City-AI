import React,{useState,useEffect} from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';
import MapView, { Marker } from 'react-native-maps';


export default function App(){
const [inc,setInc]=useState([]);
const [bus,setBus]=useState([]);
const [rep,setRep]=useState("");


useEffect(()=>{
const t=setInterval(async()=>{
setInc(await (await fetch("https://your-api/incidents")).json());
setBus(await (await fetch("https://your-api/buses")).json());
},5000);
return ()=>clearInterval(t);
},[]);


return(
<View style={{flex:1}}>
<MapView style={{flex:1}} initialRegion={{latitude:6.4529,longitude:7.5105,latitudeDelta:0.05,longitudeDelta:0.05}}>
{inc.map((i,ix)=>(<Marker key={ix} coordinate={{latitude:i.lat,longitude:i.lon}} title={i.incident_type}/>))}
{bus.map((b,ix)=>(<Marker key={ix+1000} coordinate={{latitude:b.lat,longitude:b.lon}} pinColor="blue" title={b.id}
</MapView>
<View style={styles.card}>
<Text>Report Incident</Text>
<TextInput value={rep} onChangeText={setRep} style={styles.box}/>
<Button title="Submit" onPress={()=>setRep("")}/>
</View>
</View>
);
}
const styles=StyleSheet.create({card:{position:'absolute',bottom:20,left:10,right:10,backgroundColor:'#fff',padding:10},box:{borderWidth:1,borderColor:'#ccc',marginVertical:5}});

import axios from "axios";
import { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get("http://localhost:5001/api/data")
      .then(response => setData(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Data from backend:</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
