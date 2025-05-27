<div class="moderator-list" style="display: flex; flex-wrap: wrap; gap: 16px;">
  <mat-card *ngFor="let moderator of moderators" class="moderator-card" style="width: 200px; background-color: #ffffff;">
    <img mat-card-image [src]="moderator.imageData" alt="{{moderator.firstName}}">
    <mat-card-content>
      <h3 style="color: #e10000;">{{ moderator.firstName }} {{ moderator.lastName }}</h3>
    </mat-card-content>
    <mat-card-actions>
      <button mat-raised-button color="warn" (click)="deleteModerator(moderator.id!)">Delete</button>
    </mat-card-actions>
  </mat-card>
</div>