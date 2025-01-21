
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricCurrentModule import ElectricCurrent



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class AdsorptionCurrent(ElectricCurrent, ElectrochemicalQuantity):
    """
    Class representing the `AdsorptionCurrent` entity, which inherits from:
    - ElectricCurrent, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_214d925c_76c4_4f69_9afc_056a1ea82fc6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AdsorptionCurrent'`
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
    obj = AdsorptionCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_214d925c_76c4_4f69_9afc_056a1ea82fc6',
    
    class_name='AdsorptionCurrent',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_214d925c_76c4_4f69_9afc_056a1ea82fc6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AdsorptionCurrent',
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
    

    
    

    

    