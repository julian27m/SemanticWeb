import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { environment } from '../../environments/environment';
import { Articulo } from './articulo';

@Injectable({
  providedIn: 'root'
})
export class ArticuloService {
  private apiUrl = environment.apiUrl;
  private articulos: Articulo[] = [];

  constructor(
    private http: HttpClient
  ) { }

  darArticulos(): Observable<Articulo[]> {
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${sessionStorage.getItem('token')}`
    });
    return this.http.get<Articulo[]>(`${this.apiUrl}/articulos`, { headers: headers });
  }

  darArticulo(id: number): Observable<Articulo> {
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${sessionStorage.getItem('token')}`
    });
    return this.http.get<Articulo>(`${this.apiUrl}/articulo/${id}`, { headers: headers });
  }

  crearArticulo(archivo: File): Observable<Articulo> {
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${sessionStorage.getItem('token')}`
    });
    const formData = new FormData();
    formData.append('archivo', archivo);
    return this.http.post<Articulo>(`${this.apiUrl}/articulos`, formData, { headers: headers });
  }

  // Método para obtener todos los artículos
  getAllArticulos(): Articulo[] {
    return this.articulos;
  }

  // Método para almacenar los artículos obtenidos desde el servidor
  setArticulos(articulos: Articulo[]): void {
    this.articulos = articulos;
  }
}
