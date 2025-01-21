
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ProductModule import Product



from .ObjectModule import Object







class ManufacturedProduct(Product, Object):
    """
    Class representing the `ManufacturedProduct` entity, which inherits from:
    - Product, Object

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_86ca9b93_1183_4b65_81b8_c0fcd3bba5ad'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ManufacturedProduct'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ManufacturedProduct(
    
    class_iri='https://w3id.org/emmo#EMMO_86ca9b93_1183_4b65_81b8_c0fcd3bba5ad',
    
    class_name='ManufacturedProduct',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_86ca9b93_1183_4b65_81b8_c0fcd3bba5ad',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ManufacturedProduct',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    