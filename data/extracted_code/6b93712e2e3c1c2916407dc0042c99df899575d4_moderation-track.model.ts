import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ModeratorService } from '../../services/moderator.service';
import { Moderator } from '../../services/moderator.model';

@Component({
  selector: 'app-moderators',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './moderators.component.html',
  styleUrls: ['./moderators.component.scss']
})
export class ModeratorsComponent implements OnInit {

  moderators: Moderator[] = [];
  firstName: string = '';
  lastName: string = '';
  selectedFile: File | null = null;
  imagePreview: string | ArrayBuffer | null = null;

  constructor(private moderatorService: ModeratorService) {}

  ngOnInit(): void {
    this.loadModerators();
  }

  loadModerators(): void {
    this.moderatorService.getModerators().subscribe(data => {
      this.moderators = data;
    });
  }

  onFileSelected(event: any): void {
    const file = event.target.files[0];
    if (file) {
      this.selectedFile = file;

      const reader = new FileReader();
      reader.onload = () => {
        this.imagePreview = reader.result;
      };
      reader.readAsDataURL(file);
    }
  }

  addModerator(): void {
    if (!this.firstName || !this.lastName || !this.selectedFile) {
      alert('Please fill all fields and select an image.');
      return;
    }

    const formData = new FormData();
    formData.append('firstName', this.firstName);
    formData.append('lastName', this.lastName);

    if (this.selectedFile) {
      formData.append('image', this.selectedFile);
    }

    this.moderatorService.addModerator(formData).subscribe(() => {
      this.loadModerators();
      this.firstName = '';
      this.lastName = '';
      this.selectedFile = null;
      this.imagePreview = null;
    });
  }

  deleteModerator(id: string): void {
    this.moderatorService.deleteModerator(id).subscribe(() => {
      this.loadModerators();
    });
  }
}