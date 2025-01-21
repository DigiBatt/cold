
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalPlotModule import ElectrochemicalPlot







class CurrentPotentialPlot(ElectrochemicalPlot):
    """
    Class representing the `CurrentPotentialPlot` entity, which inherits from:
    - ElectrochemicalPlot

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b9a72491_8a50_4cac_a131_1e95d72b57ee'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CurrentPotentialPlot'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CurrentPotentialPlot(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b9a72491_8a50_4cac_a131_1e95d72b57ee',
    
    class_name='CurrentPotentialPlot',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b9a72491_8a50_4cac_a131_1e95d72b57ee',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CurrentPotentialPlot',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    