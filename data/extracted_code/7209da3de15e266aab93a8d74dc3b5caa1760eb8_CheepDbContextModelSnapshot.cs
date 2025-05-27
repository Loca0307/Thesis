            modelBuilder.Entity("Core.Notification", b =>
                {
                    b.Property<int>("cheepID")
                        .HasColumnType("INTEGER");

                    b.Property<int>("authorID")
                        .HasColumnType("INTEGER");

                    b.Property<string>("authorToNotifyId")
                        .HasColumnType("TEXT");

                    b.Property<bool>("tagNotification")
                        .HasColumnType("INTEGER");

                    b.HasKey("cheepID", "authorID");

                    b.HasIndex("authorToNotifyId");

                    b.ToTable("notifications");
                });
