import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ArticuloService } from '../articulo.service';
import { environment } from 'src/environments/environment';
import { Articulo } from '../articulo';

@Component({
  selector: 'app-articulo-detalle',
  templateUrl: './articulo-detalle.component.html',
  styleUrls: ['./articulo-detalle.component.css']
})
export class ArticuloDetalleComponent implements OnInit {
  articulo: Articulo | undefined;

  private apiUrl = environment.apiUrl;

  constructor(
    private route: ActivatedRoute,
    private articuloService: ArticuloService
  ) { }

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    const token = sessionStorage.getItem('token');

    if (token) {
      this.articuloService.darArticulo(id).subscribe(
        data => {
          this.articulo = data;
        },
        error => {
          console.error('Error al obtener el artículo', error);
        }
      );
    }
  }

  getRutaPdf(rutaPdf: string): string {
    const rutaRelativa = rutaPdf.replace('DescargasPDFs/', '');
    return `${this.apiUrl}/descargar/${encodeURIComponent(rutaRelativa)}`;
  }
}
