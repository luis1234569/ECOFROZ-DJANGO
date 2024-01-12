def gestionaTransporte2n(request):
    queryset = request.GET.get("buscar")
    if queryset:
        
        q1 = DetSolicitudTransporte.objects.select_related('numpedido').filter(numpedido__estado1n=2).exclude(
                numpedido__anula=True).exclude(Q(numpedido__estado2n=2) | Q(numpedido__estado2n=3) | Q(numpedido__estado2n=4)).exclude(numpedido__tipo=3).order_by('-numpedido__fchaprueba1n')

        query_nuevas = q1.filter(
            Q(numpedido__numpedido__icontains = queryset) |
            Q(numpedido__usuario_solicita__last_name__icontains = queryset) |
            Q(numpedido__usuario_solicita__first_name__icontains = queryset) |
            Q(numpedido__transportista__icontains = queryset))
        
        q2 = DetSolicitudTransporte.objects.select_related('numpedido').filter(numpedido__estado2n=2).exclude(numpedido__tipo=3).order_by('-numpedido__fchaprueba1n')
        
        query_proceso = q2.filter(
            Q(numpedido__numpedido__icontains = queryset) |
            Q(numpedido__usuario_solicita__last_name__icontains = queryset) |
            Q(numpedido__usuario_solicita__first_name__icontains = queryset) |
            Q(numpedido__transportista__icontains = queryset))
        
        q3 = DetSolicitudTransporte.objects.select_related('numpedido').filter(numpedido__estado2n=4).exclude(numpedido__tipo=3).order_by('-numpedido__fchaprueba1n')
          
        query_confirmadas = q3.filter(
            Q(numpedido__numpedido__icontains = queryset) |
            Q(numpedido__usuario_solicita__last_name__icontains = queryset) |
            Q(numpedido__usuario_solicita__first_name__icontains = queryset) |
            Q(numpedido__transportista__icontains = queryset))
        
        countn = q1.count()
        countp = q2.count()
        countc = q3.count()
          
    else:
       
        # queryset = DetSolicitudTransporte.objects.select_related('numpedido').filter(numpedido__estado1n=2).filter(
        #     Q(numpedido__estado2n=2) |
        #     Q(numpedido__estado2n=3) |
        #     Q(numpedido__estado2n=4)).exclude(
        #     numpedido__anula=True).order_by('-numpedido__fchaprueba1n')
    
        queryset = None
        query_nuevas = DetSolicitudTransporte.objects.select_related('numpedido').filter(numpedido__estado1n=2).exclude(
                numpedido__anula=True).exclude(Q(numpedido__estado2n=2) | Q(numpedido__estado2n=3) | Q(numpedido__estado2n=4)).exclude(numpedido__tipo=3).order_by('-numpedido__fchaprueba1n')
            
        query_proceso = DetSolicitudTransporte.objects.select_related('numpedido').filter(numpedido__estado2n=2).exclude(numpedido__tipo=3).order_by('-numpedido__fchaprueba1n')
            
        query_confirmadas = DetSolicitudTransporte.objects.select_related('numpedido').filter(numpedido__estado2n=4).exclude(numpedido__tipo=3).order_by('-numpedido__fchaprueba1n')[:100]
        query_confirmadast = DetSolicitudTransporte.objects.select_related('numpedido').filter(numpedido__estado2n=4).exclude(numpedido__tipo=3).order_by('-numpedido__fchaprueba1n')
        
        countn = query_nuevas.count()
        countp = query_proceso.count()
        countc = query_confirmadast.count()  

        
    return render(request, 'procesosAdministrativos/gestionar_solicitudes_transporte_2n.html', {'form2':query_nuevas, 'form3':query_proceso,'form4':query_confirmadas,'busqueda':queryset,'countn':countn,'countp':countp,'countc':countc})

