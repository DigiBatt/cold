
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalTestingModule import ElectrochemicalTesting







class Dielectrometry(ElectrochemicalTesting):
    """
    Class representing the `Dielectrometry` entity, which inherits from:
    - ElectrochemicalTesting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Dielectrometry'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Dielectrometry'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Dielectrometry(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#Dielectrometry',
    
    class_name='Dielectrometry',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Dielectrometry',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Dielectrometry',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    