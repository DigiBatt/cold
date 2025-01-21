
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CategorizedPhysicalQuantityModule import CategorizedPhysicalQuantity







class Intensive(CategorizedPhysicalQuantity):
    """
    Class representing the `Intensive` entity, which inherits from:
    - CategorizedPhysicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_602397bd_e302_42a6_be33_fe67ea81933a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Intensive'`
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
    obj = Intensive(
    
    class_iri='https://w3id.org/emmo#EMMO_602397bd_e302_42a6_be33_fe67ea81933a',
    
    class_name='Intensive',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_602397bd_e302_42a6_be33_fe67ea81933a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Intensive',
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
    

    
    

    

    