
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ProductModule import Product







class CommercialProduct(Product):
    """
    Class representing the `CommercialProduct` entity, which inherits from:
    - Product

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_00b85655_f20c_4e83_b90e_094e8ea7e48f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CommercialProduct'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CommercialProduct(
    
    class_iri='https://w3id.org/emmo#EMMO_00b85655_f20c_4e83_b90e_094e8ea7e48f',
    
    class_name='CommercialProduct',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_00b85655_f20c_4e83_b90e_094e8ea7e48f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CommercialProduct',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    