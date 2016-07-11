#pragma once

#ifndef _INIT_INCLUDE_
#define _INIT_INCLUDE_

#include "product.h"
#include "worker.h"

void init_products(std::vector<product>& list_of_products); 

void init_product(std::vector<product>& list_of_products, worker& worker); 

void init_sys_params(std::string dat, unsigned int& t_max, unsigned int& max_minute, unsigned int& max_prod_status, unsigned int& out_start);

#endif
