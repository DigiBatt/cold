
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class ElectrochemicalTransportQuantity(ElectrochemicalQuantity):
    """
    Class representing the `ElectrochemicalTransportQuantity` entity, which inherits from:
    - ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4a450a27_b84a_4c70_a3a9_15ec30e2f30b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalTransportQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalTransportQuantity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4a450a27_b84a_4c70_a3a9_15ec30e2f30b',
    
    class_name='ElectrochemicalTransportQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4a450a27_b84a_4c70_a3a9_15ec30e2f30b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalTransportQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    