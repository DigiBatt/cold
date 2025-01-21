
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AreaDensityModule import AreaDensity



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class MassLoading(AreaDensity, ElectrochemicalQuantity):
    """
    Class representing the `MassLoading` entity, which inherits from:
    - AreaDensity, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c955c089_6ee1_41a2_95fc_d534c5cfd3d5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MassLoading'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MassLoading(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c955c089_6ee1_41a2_95fc_d534c5cfd3d5',
    
    class_name='MassLoading',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c955c089_6ee1_41a2_95fc_d534c5cfd3d5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MassLoading',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    