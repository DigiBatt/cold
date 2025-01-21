
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalPlotModule import ElectrochemicalPlot







class PotentialTimePlot(ElectrochemicalPlot):
    """
    Class representing the `PotentialTimePlot` entity, which inherits from:
    - ElectrochemicalPlot

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cd7d24a5_db31_4d76_97d9_367c809f099e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PotentialTimePlot'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PotentialTimePlot(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cd7d24a5_db31_4d76_97d9_367c809f099e',
    
    class_name='PotentialTimePlot',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cd7d24a5_db31_4d76_97d9_367c809f099e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PotentialTimePlot',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    