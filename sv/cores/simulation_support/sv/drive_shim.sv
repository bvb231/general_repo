module drive_shim;
   export "DPI-C" function  drive_to_bus;
   
   typedef byte byte_queue_t [$]; 

   byte_queue_t byte_q;

   byte_queue_t drive_q [$];



   function void drive_to_bus (input byte v[]);
      byte_q = v;
  //    drive_q.push_back(byte_q);
   //   byte_q.delete();
   endfunction
   


endmodule
