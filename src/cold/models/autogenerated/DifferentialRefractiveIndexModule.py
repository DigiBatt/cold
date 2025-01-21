
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OpticalTestingModule import OpticalTesting







class DifferentialRefractiveIndex(OpticalTesting):
    """
    Class representing the `DifferentialRefractiveIndex` entity, which inherits from:
    - OpticalTesting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DifferentialRefractiveIndex'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DifferentialRefractiveIndex'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DifferentialRefractiveIndex(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#DifferentialRefractiveIndex',
    
    class_name='DifferentialRefractiveIndex',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DifferentialRefractiveIndex',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DifferentialRefractiveIndex',
        alias="class_name"
    )
    

    
    

    

    