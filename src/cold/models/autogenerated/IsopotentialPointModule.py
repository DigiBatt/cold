
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialModule import ElectricPotential



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class IsopotentialPoint(ElectricPotential, ElectrochemicalQuantity):
    """
    Class representing the `IsopotentialPoint` entity, which inherits from:
    - ElectricPotential, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ff7797ed_9ef7_40d0_872b_2c215cd54578'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IsopotentialPoint'`
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
    obj = IsopotentialPoint(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ff7797ed_9ef7_40d0_872b_2c215cd54578',
    
    class_name='IsopotentialPoint',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ff7797ed_9ef7_40d0_872b_2c215cd54578',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IsopotentialPoint',
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
    

    
    

    

    