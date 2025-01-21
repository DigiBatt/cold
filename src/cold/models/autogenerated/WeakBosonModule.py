
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GaugeBosonModule import GaugeBoson







class WeakBoson(GaugeBoson):
    """
    Class representing the `WeakBoson` entity, which inherits from:
    - GaugeBoson

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1dcc2b31_7ff4_49ed_a1bc_6e4c055c951c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'WeakBoson'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = WeakBoson(
    
    class_iri='https://w3id.org/emmo#EMMO_1dcc2b31_7ff4_49ed_a1bc_6e4c055c951c',
    
    class_name='WeakBoson',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1dcc2b31_7ff4_49ed_a1bc_6e4c055c951c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'WeakBoson',
        alias="class_name"
    )
    

    
    

    

    