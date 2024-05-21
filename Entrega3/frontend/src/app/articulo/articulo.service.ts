import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment'
import { Articulo } from './articulo';

@Injectable({
  providedIn: 'root'
})
export class ArticuloService {

  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }

  darArticulos(): Observable<Articulo[]> {
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${sessionStorage.getItem('token')}`
    });
    return this.http.get<Articulo[]>(`${this.apiUrl}/articulos`, { headers });
  }

  darArticulo(id: number): Observable<Articulo> {
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${sessionStorage.getItem('token')}`
    });
    return this.http.get<Articulo>(`${this.apiUrl}/articulo/${id}`, { headers });
  }
  

  crearArticulo(archivo: File): Observable<Articulo> {
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${sessionStorage.getItem('token')}`
    });
    const formData: FormData = new FormData();
    formData.append('archivo', archivo, archivo.name);
    return this.http.post<Articulo>(`${this.apiUrl}/articulos`, formData, { headers });
  }

  borrarArticulo(idArticulo: number): Observable<void> {
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${sessionStorage.getItem('token')}`
    });
    return this.http.delete<void>(`${this.apiUrl}/articulo/${idArticulo}`, { headers });
  }
}
