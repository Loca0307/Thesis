        if (Input.GetMouseButtonDown(2))
        {
            mouseWorldPosStart = GetPerspectivePos();
        }
        if (Input.GetMouseButton(2))
        {
            Pan();
        }
    }
    private void Pan()
    {
        if ((Input.GetAxis("Mouse Y")!=0) || (Input.GetAxis("Mouse X") != 0))
        {
            Vector3 mouseWorldPosDiff = mouseWorldPosStart - GetPerspectivePos();
            transform.position += mouseWorldPosDiff;
        }
    }
    public void FitToScreen()
    {
        //Camera.main.fieldOfView = defaultFieldOfView;
        //Bounds bound = GetBound(parentModel);
        //Vector3 boundSize = bound.size;
        //float boundDiagonal = Mathf.Sqrt((boundSize.x * boundSize.x) + (boundSize.y * boundSize.y) + (boundSize.z * boundSize.z));
        //float camDistanceToBoundCentre = boundDiagonal/2.0f/(Mathf.Tan(Camera.main.fieldOfView / 2.0f * Mathf.Deg2Rad));
        //float camDistanceToBoundWithOffset = camDistanceToBoundCentre + boundDiagonal/2.0f - (Camera.main.transform.position - transform.position).magnitude;
        //transform.position = bound.center + (-transform.forward + camDistanceToBoundWithOffset);
    }
    public Vector3 GetPerspectivePos()
    {
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        Plane plane = new Plane(transform.forward, 0.0f);
        float dist;
        plane.Raycast(ray, out dist);
        return ray.GetPoint(dist);