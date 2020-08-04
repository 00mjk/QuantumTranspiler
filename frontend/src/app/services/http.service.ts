import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { HttpHeaders } from '@angular/common/http';
import { MatSnackBar } from '@angular/material/snack-bar';

const url = "http://localhost:5000/"

// const httpOptions = {
//   headers: new HttpHeaders({
//     'Content-Type':  'application/json',
//   }),
//   responseType: 'text' as 'text'
// };
const headers = new HttpHeaders({
  'Content-Type': 'application/json',
})

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private http: HttpClient, private snackbar: MatSnackBar) { }

  async computeCircuit(input_circuit: {}, path: string) {
    let data = JSON.stringify(input_circuit)
    try {
      let circuit = await this.http.post(url + path, data, { headers, responseType: 'text' }).toPromise()
      this.snackbar.open("Successfully converted the circuit implementation.");
      return circuit
    } catch (err) {
      console.log(err)
      this.snackbar.open("Error at handling the given circuit implementation.");
    }

  }

  async exportCircuit(circuit: {}) {
    let data = JSON.stringify(circuit)
    try {
      let exportCircuit = await this.http.post(url + "export_circuit", data, { headers, responseType: 'text' }).toPromise()
      this.snackbar.open("Successfully converted to " + circuit["selectedOption"] + ".");
      return exportCircuit
    } catch (err) {
      console.log(err)
      this.snackbar.open("Error at handling the given circuit implementation.");
    }
  }
}
