import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { environment } from '../../environments/environment'
import { Tarea } from './tarea';

@Injectable({
  providedIn: 'root'
})
export class TareaService {

  private apiUrl = environment.apiUrl;

  constructor(
    private http: HttpClient
  ) { }

  darTareas(): Observable<Tarea[]> {
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${sessionStorage.getItem('token')}`
    })
    return this.http.get<Tarea[]>(`${this.apiUrl}/tareas`, { headers: headers })
  }

  darTarea(id: number): Observable<Tarea> {
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${sessionStorage.getItem('token')}`
    })
    return this.http.get<Tarea>(`${this.apiUrl}/tarea/${id}`, { headers: headers })
  }

  crearTarea(tarea: Tarea): Observable<Tarea> {
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${sessionStorage.getItem('token')}`
    })
    return this.http.post<Tarea>(`${this.apiUrl}/tareas`, tarea, { headers: headers })
  }

  editarTarea(tarea: Tarea): Observable<Tarea> {
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${sessionStorage.getItem('token')}`
    })
    return this.http.put<Tarea>(`${this.apiUrl}/tarea/${tarea.id}`, tarea, { headers: headers })
  }

  borrarTarea(idTarea: number): Observable<Tarea> {
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${sessionStorage.getItem('token')}`
    })
    return this.http.delete<Tarea>(`${this.apiUrl}/tarea/${idTarea}`, { headers: headers })
  }

}
