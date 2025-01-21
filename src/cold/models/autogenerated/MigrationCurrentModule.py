
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricCurrentModule import ElectricCurrent



from .ElectrochemicalTransportQuantityModule import ElectrochemicalTransportQuantity







class MigrationCurrent(ElectricCurrent, ElectrochemicalTransportQuantity):
    """
    Class representing the `MigrationCurrent` entity, which inherits from:
    - ElectricCurrent, ElectrochemicalTransportQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_22cec04f_c7f3_4ff8_a34b_e512379c9dcb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MigrationCurrent'`
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
    obj = MigrationCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_22cec04f_c7f3_4ff8_a34b_e512379c9dcb',
    
    class_name='MigrationCurrent',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_22cec04f_c7f3_4ff8_a34b_e512379c9dcb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MigrationCurrent',
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
    

    
    

    

    