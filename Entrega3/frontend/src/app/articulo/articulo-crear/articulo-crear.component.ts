import { Component } from '@angular/core';
import { ArticuloService } from '../articulo.service';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-articulo-crear',
  templateUrl: './articulo-crear.component.html',
  styleUrls: ['./articulo-crear.component.css']
})
export class ArticuloCrearComponent {
  articuloForm: FormGroup;

  constructor(
    private articuloService: ArticuloService,
    private fb: FormBuilder,
    private router: Router,
    private toastrService: ToastrService
  ) {
    this.articuloForm = this.fb.group({
      archivo: [null]
    });
  }

  onFileSelected(event: any) {
    const file = event.target.files[0];
    this.articuloForm.patchValue({
      archivo: file
    });
  }

  onSubmit() {
    if (this.articuloForm.get('archivo')?.value) {
      this.articuloService.crearArticulo(this.articuloForm.get('archivo')?.value).subscribe(
        response => {
          console.log('Artículo creado exitosamente', response);
          this.toastrService.success('Artículo creado exitosamente', 'Éxito', { closeButton: true });
          this.router.navigate(['/articulos']);
        },
        error => {
          console.error('Error al crear el artículo', error);
          if (error.status === 409) {
            this.toastrService.error('El artículo ya hace parte de la ontología', 'Error', { closeButton: true });
          } else {
            this.toastrService.error('Error al crear el artículo', 'Error', { closeButton: true });
          }
        }
      );
    }
  }
}
